import React from 'react'
import axios from 'axios'
import UserList from './components/UserList.js'
import ProjectList from './components/ProjectList.js'
import TaskList from './components/TaskList.js'
import UserProjectList from './components/UserProjectList.js'
import ProjectTaskList from './components/ProjectTaskList.js'
import LoginForm from './components/LoginForm.js'
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
            'tasks': [],
            'token': ''
        }
    }

    obtainAuthToken(login, password) {
        axios
            .post('http://127.0.0.1:8000/api-auth-token/', {
                'username': login,
                'password': password
            })
            .then(response => {
                const token = response.data.token
                console.log('token:', token)
                localStorage.setItem('token', token)
                this.setState({
                    'token': token
                }, this.getData)
             })
            .catch(error => console.log(error))
    }

    isAuth() {
        return !!this.state.token
    }

    componentDidMount() {
        let token = localStorage.getItem('token')
        this.setState({
            'token': token
        }, this.getData)
    }

    getHeaders() {
        if (this.isAuth()) {
            return {
                'Authorization': 'Token ' + this.state.token
            }
        }
        return {}
    }

    getData() {
        let headers = this.getHeaders()

        axios
            .get('http://127.0.0.1:8000/api/users', {headers})
            .then(response => {
                const users = response.data
                this.setState({
                    'users': users
                })
            })
            .catch(error => {
                console.log(error)
                this.setState({ 'users': [] })
            })

        axios
            .get('http://127.0.0.1:8000/api/projects', {headers})
            .then(response => {
                const projects = response.data
                this.setState({
                        'projects': projects
                    })
            })
            .catch(error => {
                console.log(error)
                this.setState({ 'projects': [] })
            })

        axios
            .get('http://127.0.0.1:8000/api/tasks', {headers})
            .then(response => {
                const tasks = response.data
                this.setState({
                    'tasks': tasks
                    })
            })
            .catch(error => {
                console.log(error)
                this.setState({ 'tasks': [] })
            })
    }

    logOut() {
        localStorage.setItem('token', '')
        this.setState({
            'token': '',
        }, this.getData)
    }

    render() {
        return (
            <div>
                <BrowserRouter>
                    <nav>
                        <li> <Link to='/'>Users</Link> </li>
                        <li> <Link to='/projects'>Projects</Link> </li>
                        <li> <Link to='/tasks'>Tasks</Link> </li>
                        <li>
                        {this.isAuth() ? <button onClick={() => this.logOut()}>Logout</button> : <Link to='/login'>Login</Link> }
                        </li>
                    </nav>
                    <Routes>
                        <Route exact path='/' element={<Navigate to='/users' />} />
                        <Route exact path='/projects' element={<ProjectList projects={this.state.projects} users={this.state.users} />} />
                        <Route exact path='/tasks' element={<TaskList tasks={this.state.tasks} />} />
                        <Route exact path='/login' element={<LoginForm obtainAuthToken={(login, password) => this.obtainAuthToken(login, password)} />} />
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
