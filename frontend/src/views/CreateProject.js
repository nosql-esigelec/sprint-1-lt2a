import React, { useState, useEffect } from 'react';
import { Button } from 'primereact/button';
import Question from '../components/form/Question';
import { createProject, selectTemplate, getTemplates,getNumberOfSections, getQuestionsForSection, getSectionByAttribute, findNextSection, getNextQuestionGivenPreviousAnswer } from '../projectService';
import TemplateCard from '../components/TemplateCard';
import { Skeleton } from 'primereact/skeleton';
import { getUserId } from '../authService';

const sanitizeProject = async (project) => {
  const userId = await getUserId()
  project.created_by = userId
  // Extract only the text fields from the project object
  return Object.entries(project).reduce((acc, [key, value]) => {
    if (Array.isArray(value)) {
      // Check if the array elements are objects containing a 'text' property
      if (value.every(item => item && typeof item === 'object' && 'text' in item)) {
        acc[key] = value.map(item => item.text);
      } else {
        acc[key] = value;
      }
    } else if (value && typeof value === 'object' && 'text' in value) {
      acc[key] = value.text;
    } else {
      acc[key] = value;
    }
    return acc;
  }, {});
};
const CreateProject = ({ onProjectAdded }) => {
  const [project, setProject] = useState({
    "pid": "",
    "project_name": "",
    "project_tags": [],
    "project_type": "",
    "project_architecture": "",
    "language": null,
    "language_version": null,
    "backend_framework": null,
    "additional_configurations": null,
    "frontend_framework": null

  });
  const defaultQuestions = [
    {
      'statement': 'Project Name',
      'id':'project_name',
      'question_type': 'text',
      'is_first': true,
      'required': true,
      'section_id': 'project_info',
      'order': 1
    },
    {
      'statement': 'Tags',
      'id': 'project_tags',
      'question_type': 'chips',
      'is_first': false,
      'required': true,
      'section_id': 'project_info',
      'order': 2
    },
    {
      'statement': 'Type of Project',
      'id': 'project_type',
      'question_type': 'text',
      'is_first': false,
      'required': true,
      'section_id': 'project_info',
      'order': 3
    },
    {
      'statement': 'Architecture',
      'id': 'project_architecture',
      'question_type': 'text',
      'is_first': false,
      'required': true,
      'section_id': 'project_info',
      'order': 4
    },
  ]
  const [questions, setQuestions] = useState(defaultQuestions);
  const [currentSection, setCurrentSection] = useState('project_info');
  const [sectionStack, setSectionStack] = useState(['project_info']);
  const [currentSectionInfo, setCurrentSectionInfo] = useState({
    id: 'project_info',
    name: 'Project Information',
    order: 1,
    description: 'Define the type of project you are working on.',
    is_conditional: false

  });
  const [loading, setLoading] = useState(false);
  const [displayRecommendation, setDisplayRecommendation] = useState(false);
  const [currentSectionNumber, setCurrentSectionNumber] = useState(1);
  // Stack to keep track of sections
  const [templateRecommended, settemplateRecommended] = useState(false);
  const [activeQuestions, setActiveQuestions] = useState({});
  const [totalSections, setTotalSections] = useState(1);
  const username = JSON.parse(localStorage.getItem('userData')).username;
  const askToAI = () => {
    // Functionality to ask AI for templates
    console.log('Asking AI for recommendations...');
  };
  useEffect(() => {
    const fetchSections = async () => {
      const numSections = await getNumberOfSections();
      setTotalSections(numSections);
    };
    fetchSections();
  }, []);
  // Separate useEffect for loading questions
  useEffect(() => {
    const loadQuestions = async () => {
      setLoading(true);
      try {
      let sectionQuestions = await getQuestionsForSection(currentSection);
      if (currentSectionInfo.is_conditional === true) {
        // If the section is conditional, load from local storage
        const storedQuestions = sessionStorage.getItem(`questions`);
        if (storedQuestions) {
          sectionQuestions = JSON.parse(storedQuestions).filter(question => question.section_id === currentSectionInfo.id);
        }
      } else {
        // Otherwise, load from the database
        sectionQuestions = await getQuestionsForSection(currentSection);
      }
      if (!sectionQuestions || sectionQuestions.length === 0) {
        sectionQuestions = defaultQuestions;
      }
      setQuestions(sectionQuestions);
      const initialActiveQuestions = {};
      for (const question of sectionQuestions) {
        initialActiveQuestions[question.id] = true; // set to true to make them all initially active
      }
      setActiveQuestions(initialActiveQuestions);
      setTimeout(async () => {
        // ... (existing code)
        setLoading(false);  // Set loading to false after fetching data
      }, 500);  // Wait for 1 second (500 ms)

    } catch (error) {
        console.error("Failed to load questions:", error); 
        setLoading(false);
        // You can set default questions here if needed
      }
    };

    loadQuestions();
  }, [currentSection]);

  // Separate useEffect for initializing project state
  useEffect(() => {
    const initialProject = questions.reduce((acc, question) => {
      if (!project.hasOwnProperty(question.id)) {
        acc[question.id] = '';
      }
      return acc;
    }, { ...project });

    setProject(initialProject);
  }, [questions]);

  const handleChange = async (e, question_id) => {
    try {
    if (question_id === "project_type" ) {
      sessionStorage.removeItem('questions');
    }

    const name = e.target.name;
    const value = e.target.value;
    setProject({ ...project, [name]: value });
    let processedValue;

    if (Array.isArray(value)) {

      let array =
        // Use the text of the first object if it exists
        value.map(item => item.text)  // Extract text from each object in the array

      processedValue = array[array.length - 1];
    } else {
      processedValue = value.text;  // If it's not an object, use it as is
    }
    let nextQuestions = await getNextQuestionGivenPreviousAnswer(name, processedValue);
    let storedQuestions = sessionStorage.getItem(`questions`);
    storedQuestions = storedQuestions ? JSON.parse(storedQuestions) : [];
    // Merge the new questions with the existing stored questions
    const mergedQuestions = [...storedQuestions, ...nextQuestions];
    // Store the merged questions in local storage
    sessionStorage.setItem(`questions`, JSON.stringify(mergedQuestions));
  } catch (error) {
    console.error("Error in handleChange:", error);
    // Handle the error, maybe set some default questions or show an error message
  }
};

  const handleNextSection = async () => {
    const nextSection = await findNextSection(currentSection);
    if (nextSection) {
      setCurrentSection(nextSection.id);
      console.log("The previous stack is", sectionStack)
      setSectionStack([...sectionStack, nextSection.id]);
      console.log("The new stack is", sectionStack)
      setCurrentSectionInfo(nextSection); // Push next section to stack
      setCurrentSectionNumber(currentSectionNumber + 1);
      const sectionInfo = await getSectionByAttribute('id', nextSection.id);
      setCurrentSectionInfo(sectionInfo);
      

    }
  };

  const handlePrevSection = async () => {
    if (sectionStack.length > 1) {
      const newStack = [...sectionStack];
      newStack.pop(); // Remove current section
      console.log("The previous stack is", newStack)
      
      setCurrentSection(newStack[newStack.length - 1]); // Set the previous section as current
      console.log("The new stack is", newStack[newStack.length - 1])
      setSectionStack(newStack);
      // sessionStorage.removeItem('questions');
      setCurrentSectionNumber(currentSectionNumber - 1);
      const sectionInfo = await getSectionByAttribute('id', newStack[newStack.length - 1]);
      console.log("The section info is", sectionInfo)
      setCurrentSectionInfo(sectionInfo);
    }
  };
  const handleRecommendation = async () => {
    console.log("The project is", project)
    setLoading(true);
    setDisplayRecommendation(true);
    const sanitizedProject2 = await sanitizeProject(project);
    console.log("The sanitized project is", sanitizedProject2)
    const newProject = await createProject(sanitizedProject2);
    setProject(newProject);

    if (newProject) {
      const templates = await getTemplates(newProject.pid);
      settemplateRecommended(templates);
    }
    setTimeout(async () => {
      // ... (existing code)
      setLoading(false);  // Set loading to false after fetching data
    }, 500);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const sanitizedProject = await sanitizeProject(project)
    console.log("Sanitized project for submission:", sanitizedProject);

    

    console.log("The sanitizeProject is ", sanitizedProject)
    const addedProject = await createProject(sanitizedProject);
    // const templateSelected = await selectTemplate(sanitizedProject);
    onProjectAdded(addedProject);
    sessionStorage.removeItem('questions');
  };
  const handleSelection = async (e, templateSelected) => {
    console.log("The project in handleSelection is", project)
    e.preventDefault();


    // console.log("Sanitized project for submission:", project);

    // const addedProject = await createProject(sanitizedProject);
    console.log("The template selected is", templateSelected)
    const templateSelectedData = await selectTemplate(project.pid, templateSelected);
    console.log("The template selected data is", templateSelectedData)
    sessionStorage.removeItem('questions');
  };
  const isLastSection = currentSectionNumber === totalSections;


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
              questions.map((question, index) => {
                if (activeQuestions[question.id]) {
                  return (
                    <Question
                      id={question.id}
                      key={question.id}
                      type={question.question_type}
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
            )}

          <div style={{ display: 'flex', alignItems: 'center' }}>
            {currentSectionNumber > 1 && (
              <>
                <Button className="evops-btn" label="Back" onClick={handlePrevSection} type='button' />
              </>
            )}
            {!isLastSection && (
              <>
                <Button className="evops-btn" label="Next" onClick={handleNextSection} type='button' />
              </>
            )}
            {(currentSection === "additional" || isLastSection) && (
              <>
                <Button className="evops-btn" type="button" onClick={handleRecommendation} label="Get Templates ?" />
                <Button className="evops-btn" type="button" onClick={handleSubmit} label="Create" />
                {/* <Button className="evops-btn" type="submit" label="Submit" /> */}
              </>
            )}
          </div>

        </form>

        <div>
          {(displayRecommendation) && (

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
                    <Button label="Ask to our AI?" onClick={askToAI} />
                  </div>
                )
              )}
            </div>
          )}


        </div>
      </div>
    </div>
  );
};

export default CreateProject;
