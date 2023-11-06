import React from 'react';
import Question from './Question';
import { Skeleton } from 'primereact/skeleton';

const FormControls = ({ questions, project, handleChange, loading, activeQuestions }) => {
  return (
    loading ? (
      <Skeleton shape="rectangle" width="100%" height="40px" />
    ) : (
      questions.map((question, index) => {
        if (activeQuestions[question.id]) {
          return (
            <Question
              type={question.question_type}
              key={index}
              label={question.statement}
              name={question.id}
              optionLabel="text"
              value={project[question.id]}
              choices={question.options || []}
              onChange={(e) => handleChange(e, question.id)}
              optionGroupChildren="version"
              optionGroupLabel="text"
            />
          );
        }
        return null;
      })
    )
  );
};

export default FormControls;