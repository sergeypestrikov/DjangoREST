import React from 'react'
import {useParams} from 'react-router-dom'
import {Link} from 'react-router-dom'


const TaskItem = ({task}) => {
    return (
        <tr>
            <td>
                <Link to={`/tasks/${task.title}`}>{task.title}</Link>
            </td>
            <td>
                {task.text}
            </td>
        </tr>
    )
}

const ProjectTaskList = ({tasks}) => {
    var params = useParams()
    console.log(params.taskID)

    var filteredTasks = tasks.filter((task) => task.projects.includes(parseInt(params.taskID)))

    return (
        <table>
            <th>
                Title
            </th>
            <th>
                Text
            </th>
            <th>
                Actual
            </th>
            {filteredTasks.map((task) => <TaskItem task={task} />)}
        </table>
    )
}

export default ProjectTaskList