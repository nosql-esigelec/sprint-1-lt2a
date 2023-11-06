import React, { useState, useEffect } from 'react';
import TemplateList from '../components/TemplateList';
import { getAllTemplates, getTemplate, deleteTemplate } from '../templateService';
// import TemplateDetails from '../components/TemplateDetails';
// import UpdateTemplateForm from './UpdateTemplateForm';
import { Dialog } from 'primereact/dialog';
import CreateTemplate from './CreateTemplate';
import NavBar from '../components/navigation/NavBar';
import { KpiCard } from '../components/kpi';

const TemplatePage = () => {
  const [templates, setTemplates] = useState([]); // Liste des projets
  const [selectedTemplate, setSelectedTemplate] = useState(null);
  const [isModalOpen, setModalOpen] = useState(false);
  const [isDetailsModalOpen, setDetailsModalOpen] = useState(false);
  const [isEditModalOpen, setEditModalOpen] = useState(false);

  const handleTemplateAdded = (addedTemplate) => {
    console.log("In Handle Template Added", addedTemplate)
    setTemplates([...templates, addedTemplate]);
    setModalOpen(false);
  };

  const handleTemplateUpdated = (updatedTemplate) => {
    const index = templates.findIndex(p => p.tid === updatedTemplate.tid);
    console.log('In Handle Template Update', index)
    const newTemplates = [...templates];
    newTemplates[index] = updatedTemplate;
    setTemplates(newTemplates);
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
    const fetchTemplates = async () => {
      const allTemplates = await getAllTemplates();
      console.log("Trying to get all templates", allTemplates)
      setTemplates(allTemplates);
    };

    fetchTemplates();
  }, []);


  const handleOpen = async (template) => {
    console.log(`Open template: ${template.tid}`);
    // const templateDetails = await getTemplate(template.tid);
    // setSelectedTemplate(templateDetails);
    setDetailsModalOpen(true);
  };

  const handleEdit = async (template) => {
    console.log(`Template to edit: ${template.tid}`);
    // const templateDetails = await getTemplate(template.tid);
    // setSelectedTemplate(templateDetails);
    setEditModalOpen(true);

  };

  const handleDelete = async (template) => {
    console.log(`Delete template: ${template.name}`);
    // await deleteTemplate(template.tid);
    const newTemplates = templates.filter(p => p.tid !== template.tid);
    setTemplates(newTemplates);

  };

  return (
    <div>
      <NavBar onNewAction={openModal} actionLabel={"New Template"} />

      <Dialog style={{ width: '70vw' }} visible={isModalOpen} onHide={closeModal}>
        <CreateTemplate
          onTemplateAdded={handleTemplateAdded}
        />
      </Dialog>

      {/* <Dialog visible={isEditModalOpen} onHide={() => setEditModalOpen(false)}>
        <UpdateTemplateForm
          onTemplateEdited={handleTemplateUpdated}
          selectedTemplate={selectedTemplate}
        />
      </Dialog> */}

      {/* <Dialog visible={isDetailsModalOpen} onHide={() => setDetailsModalOpen(false)}>
        <TemplateDetails
          template={selectedTemplate} />
      </Dialog> */}
      <div className="flex kpi-cards">
        <KpiCard
          title={"Projets créés"}
          total={templates.length}
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
      <TemplateList
        templates={templates}
        onOpen={handleOpen}
        onEdit={handleEdit}
        onDelete={handleDelete}
      />
      {/* <TemplateList
        templates={templates}
        onOpen={handleOpen}
        onEdit={handleEdit}
        onDelete={handleDelete}
      /> */}
    </div>
  );
};

export default TemplatePage;
