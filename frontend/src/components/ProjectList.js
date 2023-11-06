import React, { useState, useRef } from 'react';
import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
import { Toast } from 'primereact/toast';
import { Button } from 'primereact/button';
import { Tag } from 'primereact/tag';
import PropTypes from 'prop-types';
import { FilterMatchMode } from 'primereact/api';
import { InputText } from 'primereact/inputtext';
import '../styles/DataTable.css'
const ProjectList = ({ projects, onOpen, onEdit, onDelete }) => {
    ProjectList.propTypes = {
        projects: PropTypes.array.isRequired,
        onOpen: PropTypes.func.isRequired,
        onEdit: PropTypes.func.isRequired,
        onDelete: PropTypes.func.isRequired,
      };
      const [filters, setFilters] = useState({
        global: { value: null, matchMode: FilterMatchMode.CONTAINS },
        project_name: { value: null, matchMode: FilterMatchMode.STARTS_WITH },
        project_type: { value: null, matchMode: FilterMatchMode.STARTS_WITH },
        project_tags: { value: null, matchMode: FilterMatchMode.IN },
        project_architecture: { value: null, matchMode: FilterMatchMode.STARTS_WITH },
        language: { value: null, matchMode: FilterMatchMode.CONTAINS },

    });
    const [globalFilterValue, setGlobalFilterValue] = useState('');
    const [selectedProjects, setSelectedProjects] = useState(null);
    const toast = useRef(null);

    // Replace this with actual CRUD operations
    const openProject = (project) => {
      onOpen(project);
  };
    const editProject = (project) => {
        onEdit(project);
    };

    const deleteProject = (project) => {
        onDelete(project);
    };
    const onGlobalFilterChange = (e) => {
      const value = e.target.value;
      let _filters = { ...filters };

      _filters['global'].value = value;

      setFilters(_filters);
      setGlobalFilterValue(value);
  };
  const renderHeader = () => {
    return (
        <div className="flex justify-content-end">
            <span className="p-input-icon-left">
                <i className="pi pi-search" />
                <InputText value={globalFilterValue} onChange={onGlobalFilterChange} placeholder="Keyword Search" />
            </span>
        </div>
    );
};
    const header = renderHeader();
    const actionBodyTemplate = (rowData) => {
        return (
            <React.Fragment>
              <Button 
                icon="pi pi-eye" 
                className="p-button-rounded p-button-success p-mr-2" 
                onClick={() => openProject(rowData)} 
                tooltip="View" 
                tooltipOptions={{ position: 'left' }}
                />
                <Button 
                icon="pi pi-pencil" 
                className="p-button-rounded p-button-success p-mr-2" 
                onClick={() => editProject(rowData)} 
                tooltip="Edit" 
                tooltipOptions={{ position: 'left' }}
                />
                <Button 
                icon="pi pi-trash" 
                className="p-button-rounded p-button-warning" 
                onClick={() => deleteProject(rowData)} 
                tooltip="Delete" 
                tooltipOptions={{ position: 'left' }}
                />
            </React.Fragment>
        );
    };
    const tagBodyTemplate = (tagData) => {
        if (tagData && Array.isArray(tagData.project_tags)) {
          return tagData.project_tags.map((tag, index) => (
            <Tag key={index} severity="info" value={tag} rounded></Tag>
          ));
        }
        return null;  // ou retourner un élément par défaut
      };
    return (
        <div>
            <Toast ref={toast} />
            <div className="card">
                <DataTable value={projects} 
                selection={selectedProjects} 
                onSelectionChange={e => setSelectedProjects(e.value)}
                dataKey="pid" 
                paginator 
                rows={10}
                filters={filters} 
                filterDisplay="row"
                header={header}
                globalFilterFields={['project_name', 'project_type', 'project_architecture', 'project_tags', 'language']} >
                    
                    {/* Replace these columns with your actual project fields */}
                    <Column key="project_name" field="project_name" header="Name" filter filterPlaceholder='By name'></Column>
                    <Column key="project_type" field="project_type" header="Type" filter filterPlaceholder='By type'></Column>
                    
                    <Column key="project_architecture" field="project_architecture" filter filterPlaceholder='By architecture' header="Architecture"></Column>
                    <Column key="project_tags" field="project_tags" header="Tags" filter filterPlaceholder='By tags' body={tagBodyTemplate}></Column>
                    <Column key="buttons" body={actionBodyTemplate}></Column>
                </DataTable>
            </div>
        </div>
    );
};

export default ProjectList;