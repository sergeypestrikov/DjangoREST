import React from 'react'


class ProjectForm extends React.Component {
    constructor(props) {
        super(props)
//        console.log(props)

//        this.obtainAuthToken = props.obtainAuthToken
        this.state = {
            'title': '',
            'users': []
        }
    }

    handleChange(event) {
        this.setState({
            [event.target.name]: event.target.value
        })
    }

    handleUsersSelect(event) {
        if (!event.target.selectedOptions) {
            this.setState({
                'users': []
                })
            return;
        }

        let users = []

        for(let option of event.target.selectedOptions) {
            users.push(option.value)
        }
        this.setState({
            'users': users
        })
    }

    handleSubmit(event) {
        this.props.createProject(this.state.title, this.state.users)
        event.preventDefault()
    }

    render() {
        return (
            <div>
                <form onSubmit={(event) => this.handleSubmit(event)}>
                    <input type="text" name="title" placeholder="title" value={this.state.title} onChange={(event) => this.handleChange(event)} />
                    <select multiple onChange={(event) => this.handleUsersSelect(event)} >
                        {this.props.users.map((user) => <option value={user.id}>{user.name}</option> )}
                    </select>
                    <input type="submit" value="Create" />
                </form>
            </div>
        )
    }
}

export default ProjectForm;
