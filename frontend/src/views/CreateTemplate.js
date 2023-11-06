import React, { useState, useEffect } from 'react';
import { Button } from 'primereact/button';
import Question from '../components/form/Question';
import { createTemplate, addTemplateForUser } from '../templateService';
import TemplateCard from '../components/TemplateCard';
import { Skeleton } from 'primereact/skeleton';
import { getUserId } from '../authService';

const CreateTemplate = ({ onTemplateAdded }) => {

  const defaultTemplate = {
    "tid": "",
    "template_name": "",
    "template_description": "",
    "template_tags": [],
    "template_tree": "",
    "is_private": false
  }
  const defaultQuestions = [
    {
      'statement': 'Template Name',
      'id': 'template_name',
      'question_type': 'text',
      'is_first': true,
      'required': true,
      'section_id': 'template_info',
      'order': 1
    },
    {
      'statement': 'Description',
      'id': 'template_description',
      'question_type': 'text',
      'is_first': false,
      'required': true,
      'section_id': 'template_info',
      'order': 2
    },
    {
      'statement': 'Tags',
      'id': 'template_tags',
      'question_type': 'chips',
      'is_first': false,
      'required': true,
      'section_id': 'template_info',
      'order': 3
    },
    {
      'statement': 'URL',
      'id': 'template_url',
      'question_type': 'text',
      'is_first': false,
      'required': true,
      'section_id': 'template_info',
      'order': 4
    },
    {
      'statement': 'Tree',
      'id': 'template_tree',
      'question_type': 'textarea',
      'is_first': false,
      'required': true,
      'section_id': 'template_info',
      'order': 5
    },
    {
      'statement': 'Is Private?',
      'id': 'is_private',
      'question_type': 'switch',
      'is_first': false,
      'required': true,
      'section_id': 'template_info',
      'order': 6
    },
  ]
  const [template, setTemplate] = useState(defaultTemplate)
  const [questions, setQuestions] = useState(defaultQuestions);
  const [currentSectionInfo, setCurrentSectionInfo] = useState({
    id: 'template_info',
    name: 'Template Information',
    order: 1,
    description: 'Define the template you want to add.',
    is_conditional: false

  });
  const [loading, setLoading] = useState(false);
  const username = JSON.parse(localStorage.getItem('userData')).username;
  const askToAI = () => {
    // Functionality to ask AI for templates
    console.log('Asking AI for recommendations...');
  };
  //   useEffect(() => {
  //     const fetchSections = async () => {
  //       const numSections = await getNumberOfSections();
  //       setTotalSections(numSections);
  //     };
  //     fetchSections();
  //   }, []);
  //   // Separate useEffect for loading questions
  //   useEffect(() => {
  //     const loadQuestions = async () => {
  //       setLoading(true);
  //       try {
  //       let sectionQuestions = await getQuestionsForSection(currentSection);
  //       if (currentSectionInfo.is_conditional === true) {
  //         // If the section is conditional, load from local storage
  //         const storedQuestions = sessionStorage.getItem(`questions`);
  //         if (storedQuestions) {
  //           sectionQuestions = JSON.parse(storedQuestions).filter(question => question.section_id === currentSectionInfo.id);
  //         }
  //       } else {
  //         // Otherwise, load from the database
  //         sectionQuestions = await getQuestionsForSection(currentSection);
  //       }
  //       if (!sectionQuestions || sectionQuestions.length === 0) {
  //         sectionQuestions = defaultQuestions;
  //       }
  //       setQuestions(sectionQuestions);
  //       const initialActiveQuestions = {};
  //       for (const question of sectionQuestions) {
  //         initialActiveQuestions[question.id] = true; // set to true to make them all initially active
  //       }
  //       setActiveQuestions(initialActiveQuestions);
  //       setTimeout(async () => {
  //         // ... (existing code)
  //         setLoading(false);  // Set loading to false after fetching data
  //       }, 500);  // Wait for 1 second (500 ms)

  //     } catch (error) {
  //         console.error("Failed to load questions:", error); 
  //         setLoading(false);
  //         // You can set default questions here if needed
  //       }
  //     };

  //     loadQuestions();
  //   }, [currentSection]);

  // Separate useEffect for initializing project state
  //   useEffect(() => {
  //     const initialProject = questions.reduce((acc, question) => {
  //       if (!project.hasOwnProperty(question.id)) {
  //         acc[question.id] = '';
  //       }
  //       return acc;
  //     }, { ...project });

  //     setProject(initialProject);
  //   }, [questions]);

  const handleChange = async (e, question_id) => {
    try {

      const name = e.target.name;
      const value = e.target.value;
      setTemplate({ ...template, [name]: value });
      
    } catch (error) {
      console.error("Error in handleChange:", error);
      // Handle the error, maybe set some default questions or show an error message
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const userId = await getUserId()

    template.created_by = userId
    console.log("The template is ", template)
    
    const addedTemplate = await createTemplate(template);


    // // const templateSelected = await selectTemplate(sanitizedProject);
    // onTemplateAdded(addedTemplate);

  };


  return (
    <div className="flex align-items-center justify-content-center">
      <div className="p-8 w-full">

        <h2>{currentSectionInfo.name}</h2>
        <p>{currentSectionInfo.description}</p>



        <form onSubmit={handleSubmit}>
          {
            loading ? (
              <Skeleton shape="rectangle" width="100%" height="40px" />
            ) : (
              defaultQuestions.map((question, index) => {
                console.log("The questions are", defaultQuestions[question.id])

                return (
                  <Question
                    id={question.id}
                    key={question.id}
                    type={question.question_type}
                    label={question.statement}
                    name={question.id}
                    optionLabel="text"
                    value={template[question.id]}
                    choices={question.options || []}
                    onChange={(e) => handleChange(e, question.id)}
                    optionGroupChildren="version"
                    optionGroupLabel="text"
                  />
                );


              })
            )}

          <div style={{ display: 'flex', alignItems: 'center' }}>


            <Button className="evops-btn" type="button" onClick={handleSubmit} label="Create" />

          </div>

        </form>

        <div>



        </div>
      </div>
    </div>
  );
};

export default CreateTemplate;
