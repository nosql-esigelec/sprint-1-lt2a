import React, { useState } from 'react';
import { Button } from 'primereact/button';
import '../styles/TemplateCard.css';

const TemplateCard = ({ template, onValidate, onEdit, onViewTree }) => {
  const [showTree, setShowTree] = useState(false);
  const onViewTrees = (template) => {
    console.log("Viewing tree ?:", showTree);
    console.log("Viewing tree for template:", template);
  };
  const isGitHubUrl = (url) => {
    return url && url.includes('github.com');
  };

  return (
    <div className="template-card ">
    <div className="flex-row ">
      {/* Header Row */}
      <div className="info-column">
        <h3>{template.template_name}</h3>
        <p>{template.template_description}</p>
        {template.template_url && (
          <a href={template.template_url} target="_blank" rel="noopener noreferrer">
            {isGitHubUrl(template.url) ? (
              <i className="pi pi-github" style={{ fontSize: '1.5em' }}></i>
            ) : (
              <i className="pi pi-external-link" style={{ fontSize: '1.5em' }}></i>
            )}
          </a>
        )}
      </div>
      
      <div className="actions-column">
          <Button className="evops-btn" icon="pi pi-check" onClick={(e) => onValidate(e, template)} />
          {/* <Button className="evops-btn" icon="pi pi-pencil" onClick={() => onEdit(template)} /> */}
          <Button 
          className="evops-btn" 
          icon="pi pi-folder-open" 
          onClick={() => { onViewTrees(template); setShowTree(true); }} 
        //   onMouseOver={() => { onViewTrees(template); setShowTree(true); }} 
        //   onMouseOut={() => setShowTree(false)}
          />
      </div>


    </div>
    <div className={`tree-container ${showTree ? 'show' : ''}`}>
        {/* Your tree structure here. For demonstration, using <pre> tags */}
        <pre>
         {template.template_tree}
        </pre>
      </div>
    </div>
  );
};

export default TemplateCard;
