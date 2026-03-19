import React, { useEffect, useState } from 'react';

const Workouts = () => {
  const [workouts, setWorkouts] = useState([]);
  const codespaceEndpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;
  const apiBase = process.env.REACT_APP_CODESPACE_NAME
    ? codespaceEndpoint.replace('/api/workouts/', '')
    : window.location.hostname.includes('-3000.app.github.dev')
      ? `${window.location.protocol}//${window.location.hostname.replace('-3000.app.github.dev', '-8000.app.github.dev')}`
      : 'http://127.0.0.1:8000';
  const endpoint = `${apiBase}/api/workouts/`;

  useEffect(() => {
    console.log('Fetching Workouts from:', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = Array.isArray(data) ? data : data.results || [];
        setWorkouts(results);
        console.log('Fetched Workouts:', data);
      })
      .catch(err => console.error('Error fetching workouts:', err));
  }, [endpoint]);

  return (
    <div className="card mb-4">
      <div className="card-body">
        <h2 className="card-title mb-4">Workouts</h2>
        <div className="table-responsive">
          <table className="table table-striped table-bordered">
            <thead className="table-dark">
              <tr>
                {workouts.length > 0 && Object.keys(workouts[0]).map((key) => (
                  <th key={key}>{key.charAt(0).toUpperCase() + key.slice(1)}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {workouts.map((workout, idx) => (
                <tr key={workout.id || idx}>
                  {Object.values(workout).map((val, i) => (
                    <td key={i}>{typeof val === 'object' ? JSON.stringify(val) : val}</td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
          {workouts.length === 0 && <div className="alert alert-info">No workouts found.</div>}
        </div>
      </div>
    </div>
  );
};

export default Workouts;
