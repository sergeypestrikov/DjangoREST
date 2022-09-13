import React from 'react'


const ProjectItem = ({project, users, deleteProject}) => {
    return (
        <tr>
            <td>
                {project.title}
            </td>
            <td>
                {project.users.map(userID => users.find(a => a.id == userID).name) }
            </td>
            <td>
                <button onClick={() => deleteProject(project.id) }>Delete</button>
            </td>
        </tr>
    )
}

const ProjectList = ({projects, users, deleteProject}) => {
    return (
        <table>
            <th>
                Title
            </th>
            <th>
                Users
            </th>
            {projects.map((project) => <ProjectItem project={project} users={users} deleteProject={deleteProject}/> )}
        </table>
    )
}

export default ProjectList