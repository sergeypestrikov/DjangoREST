import React from 'react'
import {Link} from 'react-router-dom'


const UserItem = ({user}) => {
    return (
        <tr>
            <td>
                <Link to={`/users/${user.id}`}>{user.username}</Link>
            </td>
            <td>
                {user.name}
            </td>
            <td>
                {user.add_info}
            </td>
            <td>
                {user.email}
            </td>
        </tr>
    )
}

const UserList = ({users}) => {
    return (
        <table>
            <th>
                Username
            </th>
            <th>
                Name
            </th>
            <th>
                Add_info
            </th>
            <th>
                Email
            </th>
            {users.map((user) => <UserItem user={user} />)}
        </table>
    )
}

export default UserList