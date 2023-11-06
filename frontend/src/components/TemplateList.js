// Implement the template List using the TemplateCard component, templaes should be a props
import React, { useState, useRef } from 'react';
import TemplateCard from './TemplateCard';
import PropTypes from 'prop-types'; 
import { Skeleton } from 'primereact/skeleton';
import { Card } from 'primereact/card';
import { Button } from 'primereact/button';
import { Dialog } from 'primereact/dialog';

const TemplateList = ({ templates, onOpen, onEdit, onDelete }) => {
    TemplateList.propTypes = {
        templates: PropTypes.array.isRequired,
        onOpen: PropTypes.func.isRequired,
        onEdit: PropTypes.func.isRequired,
        onDelete: PropTypes.func.isRequired,
    };
    const [isModalOpen, setModalOpen] = useState(false);
    const [selectedTemplate, setSelectedTemplate] = useState(null);
    
    const openTemplate = (template) => {
        onOpen(template);
    };
    const editTemplate = (template) => {
        onEdit(template);
    };
    
    const deleteTemplate = (template) => {
        onDelete(template);
    };
    const openModal = () => setModalOpen(true);
    const closeModal = () => setModalOpen(false);
    

    return (
        <div className="p-grid p-justify-center">
        {templates.map((template) => (
            <TemplateCard
            key={template.tid}
            template={template}
            onOpen={openTemplate}
            onEdit={editTemplate}
            onDelete={deleteTemplate}
            />
        ))}
   
       
        </div>
    );
    }

    export default TemplateList;