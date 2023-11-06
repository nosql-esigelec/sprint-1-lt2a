import React, { useState } from 'react';
import { updateProject } from '../projectService'; 
import Question from '../components/form/Question';
import { Button } from 'primereact/button';

const UpdateProjectForm = ({ onProjectEdited, selectedProject }) => {
  const initialProject = { ...selectedProject, parojetc_tags: selectedProject.project_tags.join(", ") };
  const [project, setProject] = useState(initialProject);
  const handleChange = (e) => {
    const { name, value, type } = e.target;
    let updatedValue = value;
    console.log("The type is", type)
    console.log("The name is", name)
    console.log("The value is", value)

    setProject({ ...project, [name]: updatedValue });
  };
  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log("In edited, the project 1 is",selectedProject)

    await updateProject(selectedProject.pid, project);
    console.log("In edited, the project is", project)
    onProjectEdited(project);
  };

  return (
    <form onSubmit={handleSubmit}>
      <Question
      type="text"
        label="Project Name"
        name="project_name"
        placeholder="Nom du projet"
        value={project.project_name}
        onChange={handleChange}
      />
      <Question
        type="text"
        label="Project Type"
        name="project_type"
        placeholder="Type de projet"
        value={project.project_type}
        onChange={handleChange}
      />
      <Question
        type="text"
        label="Project Architecture"
        name="project_architecture"
        placeholder="Architecture de projet"
        value={project.project_architecture}
        onChange={handleChange}
      />
      <Question
        type="chips"
        label="Tags"
        name="project_tags"
        placeholder="Tags (séparés par des virgules)"
        value={ project.project_tags}
        onChange={handleChange}
      />
      <Button className="evops-btn" label="Mettre à jour" type='submit'/>
    </form>
  );
};

export default UpdateProjectForm;
