import React, { useEffect, useState } from 'react';

const Users = () => {
  const [users, setUsers] = useState([]);
  const codespaceEndpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`;
  const apiBase = process.env.REACT_APP_CODESPACE_NAME
    ? codespaceEndpoint.replace('/api/users/', '')
    : window.location.hostname.includes('-3000.app.github.dev')
      ? `${window.location.protocol}//${window.location.hostname.replace('-3000.app.github.dev', '-8000.app.github.dev')}`
      : 'http://127.0.0.1:8000';
  const endpoint = `${apiBase}/api/users/`;

  useEffect(() => {
    console.log('Fetching Users from:', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = Array.isArray(data) ? data : data.results || [];
        setUsers(results);
        console.log('Fetched Users:', data);
      })
      .catch(err => console.error('Error fetching users:', err));
  }, [endpoint]);

  return (
    <div className="card mb-4">
      <div className="card-body">
        <h2 className="card-title mb-4">Users</h2>
        <div className="table-responsive">
          <table className="table table-striped table-bordered">
            <thead className="table-dark">
              <tr>
                {users.length > 0 && Object.keys(users[0]).map((key) => (
                  <th key={key}>{key.charAt(0).toUpperCase() + key.slice(1)}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {users.map((user, idx) => (
                <tr key={user.id || idx}>
                  {Object.values(user).map((val, i) => (
                    <td key={i}>{typeof val === 'object' ? JSON.stringify(val) : val}</td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
          {users.length === 0 && <div className="alert alert-info">No users found.</div>}
        </div>
      </div>
    </div>
  );
};

export default Users;
