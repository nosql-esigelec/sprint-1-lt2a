import React, { useState, useEffect } from 'react';
import ProjectList from '../components/ProjectList';
import { getAllProjects, getProject, deleteProject } from '../projectService';
import ProjectDetails from '../components/ProjectDetails';
import UpdateProjectForm from './UpdateProjectForm';
import { Dialog } from 'primereact/dialog';
import CreateProject from './CreateProject';
import NavBar from '../components/navigation/NavBar';
import { KpiCard } from '../components/kpi';
import { getUser, getUserId } from '../authService';

const ProjectPage = () => {
  const [projects, setProjects] = useState([]); // Liste des projets
  const [selectedProject, setSelectedProject] = useState(null);
  const [isModalOpen, setModalOpen] = useState(false);
  const [isDetailsModalOpen, setDetailsModalOpen] = useState(false);
  const [isEditModalOpen, setEditModalOpen] = useState(false);

  const handleProjectAdded = (addedProject) => {
    console.log("In Handle Project Added", addedProject)
    setProjects([...projects, addedProject]);
    setModalOpen(false);
  };

  const handleProjectUpdated = (updatedProject) => {
    const index = projects.findIndex(p => p.pid === updatedProject.pid);
    console.log('In Handle Project Update', index)
    const newProjects = [...projects];
    newProjects[index] = updatedProject;
    setProjects(newProjects);
    setModalOpen(false);
  };
  // On openModal, setModalOpen to true and removve the session storage iten "questions"
  const openModal = () => {
    setModalOpen(true);
    sessionStorage.removeItem('questions');
  };
  // const openModal = () => setModalOpen(true) ;
  const closeModal = () => setModalOpen(false);


  useEffect(() => {
    const fetchProjects = async () => {
      const userId = await getUserId()
      const allProjects = await getAllProjects(userId);
      console.log("Trying to get all projects", allProjects);
  
      if (allProjects.error) {
        setProjects([]);
      } else {
        setProjects(allProjects);
      }
    };
  
    fetchProjects();
  }, []);
  


  const handleOpen = async (project) => {
    console.log(`Open project: ${project.pid}`);
    const projectDetails = await getProject(project.pid);
    setSelectedProject(projectDetails);
    setDetailsModalOpen(true);
  };

  const handleEdit = async (project) => {
    console.log(`Project to edit: ${project.pid}`);
    const projectDetails = await getProject(project.pid);
    setSelectedProject(projectDetails);
    setEditModalOpen(true);

  };

  const handleDelete = async (project) => {
    console.log(`Delete project: ${project.name}`);
    await deleteProject(project.pid);
    const newProjects = projects.filter(p => p.pid !== project.pid);
    setProjects(newProjects);

  };

  return (
    <div>
      <NavBar onNewAction={openModal} actionLabel={"New Project"} />

      <Dialog style={{ width: '70vw' }} visible={isModalOpen} onHide={closeModal}>
        <CreateProject
          onProjectAdded={handleProjectAdded}
        />
      </Dialog>

      <Dialog visible={isEditModalOpen} onHide={() => setEditModalOpen(false)}>
        <UpdateProjectForm
          onProjectEdited={handleProjectUpdated}
          selectedProject={selectedProject}
        />
      </Dialog>

      <Dialog visible={isDetailsModalOpen} onHide={() => setDetailsModalOpen(false)}>
        <ProjectDetails
          project={selectedProject} />
      </Dialog>
      <div className="flex kpi-cards">
        <KpiCard
          title={"Projets créés"}
          total={projects.length}
          icon="pi pi-folder-open"

        />
        <KpiCard
          title={"Templates disponibles"}
          total={15}
          icon="pi pi-clone"
        />
        <KpiCard
          title={"Projets en cours"}
          total={3}
          icon="pi pi-spinner"
        />
      </div>
      <ProjectList
        projects={projects}
        onOpen={handleOpen}
        onEdit={handleEdit}
        onDelete={handleDelete}
      />
    </div>
  );
};

export default ProjectPage;
