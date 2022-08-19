import React from 'react'
import axios from 'axios'
import UserList from './components/UserList.js'
import ProjectList from './components/ProjectList.js'
import TaskList from './components/TaskList.js'
import UserProjectList from './components/UserProjectList.js'
import ProjectTaskList from './components/ProjectTaskList.js'
import {HashRouter, BrowserRouter, Route, Routes, Link, Navigate, useLocation} from 'react-router-dom'


const NotFound = () => {
    var {pathname} = useLocation()

    return (
        <div>
            Page '{pathname}' not found
        </div>
    )
}

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
            'tasks': []
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users')
            .then(response => {
                const users = response.data.results
                    this.setState(
                    {
                        'users': users
                    }
                )
            })
            .catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/projects')
            .then(response => {
                const projects = response.data.results
                    this.setState(
                    {
                        'projects': projects
                    }
                )
            })
            .catch(error => console.log(error))

             axios.get('http://127.0.0.1:8000/api/tasks')
            .then(response => {
                const tasks = response.data.results
                    this.setState(
                    {
                        'tasks': tasks
                    }
                )
            })
            .catch(error => console.log(error))
    }

    render() {
        return (
            <div>
                <BrowserRouter>
                    <nav>
                    <li> <Link to='/'>Users</Link> </li>
                    <li> <Link to='/projects'>Projects</Link> </li>
                    <li> <Link to='/tasks'>Tasks</Link> </li>
                    </nav>
                    <Routes>
                        <Route exact path='/' element={<Navigate to='/users' />} />
                        <Route exact path='/projects' element={<ProjectList projects={this.state.projects} />} />
                        <Route exact path='/tasks' element={<TaskList tasks={this.state.tasks} />} />
                        <Route path='/users' >
                            <Route index element={<UserList users={this.state.users} />} />
                            <Route path=':userID' element={<UserProjectList projects={this.state.projects} />} />
                            <Route path=':taskID' element={<ProjectTaskList tasks={this.state.tasks} />} />
                            <Route path='projects' element={<ProjectList projects={this.state.projects} />}  />
                        </Route>
                        <Route path='*' element={<NotFound />} />

                    </Routes>
                </BrowserRouter>
            </div>
        )
    }
}

export default App;
