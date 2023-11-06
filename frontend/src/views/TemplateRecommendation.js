import React from 'react';
import TemplateCard from '../components/TemplateCard';
import { Skeleton } from 'primereact/skeleton';

const TemplateRecommendation = ({ loading, templateRecommended, handleSelection }) => {
  return (
    <div>
      <h2 className="section-title">Recommended Templates</h2>
      {loading ? (
        <Skeleton shape="rectangle" width="100%" height="40px" />
      ) : (
        templateRecommended && templateRecommended.length > 0 ? (
          templateRecommended.map((template, index) => (
            <TemplateCard
              key={index}
              template={template}
              onValidate={(e) => handleSelection(e, template)}
              onViewTree={() => { }}
            />
          ))
        ) : (
          <div>
            <p>Sorry, we don't have templates to recommend.</p>
          </div>
        )
      )}
    </div>
  );
};

export default TemplateRecommendation;