import React from 'react'


const ProjectItem = ({project, users}) => {
    return (
        <tr>
            <td>
                {project.title}
            </td>
            <td>
                {project.users.map(userID => users.find(a => a.id == userID).name) }
            </td>
        </tr>
    )
}

const ProjectList = ({projects, users}) => {
    return (
        <table>
            <th>
                Title
            </th>
            <th>
                Users
            </th>
            {projects.map((project) => <ProjectItem project={project} users={users} />)}
        </table>
    )
}

export default ProjectList