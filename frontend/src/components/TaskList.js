import React from 'react'
import {useParams} from 'react-router-dom'


const TaskItem = ({task}) => {
    return (
        <tr>
            <td>
                {task.title}
            </td>
            <td>
                {task.text}
            <td>
                {task.actual}
            </td>
            </td>
        </tr>
    )
}

const TaskList = ({tasks}) => {
//    var {tasks} = useParams()
//    console.log(tasks)
//
//    var filtertasks = tasks.filter((task) => task.tasks.includes(tasks))

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
            {tasks.map((task) => <TaskItem task={task} />)}
        </table>
    )
}

export default TaskList