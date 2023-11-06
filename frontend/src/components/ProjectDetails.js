import React from 'react';

const ProjectDetails = ({ project }) => {
  if (!project) return null;

  return (
    <div>
      <h2>{project.project_name}</h2>
      <p>Type: {project.project_type}</p>
      {project.project_repo && <p>Repository: {project.project_repo}</p>}
      {project.project_vcs && <p>VCS: {project.vcs}</p>}
      <div>
        {project.project_tags.map((tag, index) => (
          <span key={index}>{tag}</span>
        ))}
      </div>

    </div>
  );
};

export default ProjectDetails;
