import React from 'react'
import {useParams} from 'react-router-dom'
import {Link} from 'react-router-dom'


const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>
                <Link to={`/projects/${project.title}`}>{project.title}</Link>
            </td>
            <td>
                {project.text}
            </td>
        </tr>
    )
}

const UserProjectList = ({projects}) => {
    var params = useParams()
    console.log(params.userID)

    var filteredProjects = projects.filter((project) => project.users.includes(parseInt(params.userID)))

    return (
        <table>
            <th>
                Title
            </th>
            <th>
                Users
            </th>
            {filteredProjects.map((project) => <ProjectItem project={project} />)}
        </table>
    )
}

export default UserProjectList