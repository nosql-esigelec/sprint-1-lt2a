import apiClient from "./api";

export const createProject = async (project) => {
  try {
    const response = await apiClient.post("/projects/", project);
    console.log("Create Project", response)
    return response.data;
  } catch (error) {
    // Gestion des erreurs
    console.error("An error occurred while creating the project: ", error);
    return { error: "An error occurred while creating the project." };
  }
};

export const getAllProjects = async (userId) => {
  try {
    console.log("The user id is", userId)
    const response = await apiClient.get("/projects/",
    {params: {user_id: userId}});
    console.log("Get All Projects", response)
    return response.data;
  } catch (error) {
    // Gestion des erreurs
    console.error("An error occurred while fetching the projects: ", error);
    return { error: "An error occurred while fetching all projects." };
  }
};

export const getProject = async (id) => {
  try {
    const response = await apiClient.get(`/projects/${id}`);
    return response.data;
  } catch (error) {
    // Gestion des erreurs
    console.error(`An error occurred while fetching the project with id ${id}: `, error);
  }
};

export const updateProject = async (id, updatedProject) => {
  try {
    const response = await apiClient.put(`/projects/${id}`, updatedProject);
    return response.data;
  } catch (error) {
    // Gestion des erreurs
    console.error(`An error occurred while updating the project with id ${id}: `, error);
  }
};

export const deleteProject = async (id) => {
  try {
    await apiClient.delete(`/projects/${id}`);
  } catch (error) {
    // Gestion des erreurs
    console.error(`An error occurred while deleting the project with id ${id}: `, error);
  }
};

export const getQuestionsForSection = async (sectionId) => {
  try {
    const response = await apiClient.get(`/sections/${sectionId}/questions`);
    return response.data;
  } catch (error) {
    // Gestion des erreurs
    console.error(`An error occurred while fetching the questions for section ${sectionId}: `, error);
  }
}

export const findNextSection = async (currentSectionId) => {
  try {
    const response = await apiClient.get(`/sections/${currentSectionId}/next-section`);
    return response.data;
  } catch (error) {
    console.error(`An error occurred while fetching the next section for ${currentSectionId}: `, error);
  }
};

export const create_project_selection = async (project_id, section_id, question_id, option_text) => {
  try {
    const response = await apiClient.post("/projects/", project_id, section_id, question_id, option_text);
    console.log("Create Project Section in Neo4j", response)
    return response.data;
  } catch (error) {
    console.error("An error occurred while creating the project: ", error);
  }
};

export const getNextQuestionGivenPreviousAnswer = async (question_id, option_text) => {
  try {
    const payload = {
      question_id: question_id,
      option_text: option_text
    }
    const response = await apiClient.get(`/sections/next-questions`, {params:payload});
    console.log("Next question", response)
    return response.data;
  } catch (error) {
    console.error("An error occurred while creating the project: ", error);
  }
};

export const getTemplates = async (project_id) => {
  try {
    // console.log("The project id are:",project_id)
    const response = await apiClient.get(`/projects/${project_id}/recommended-templates`);
    console.log("The templates are", response)
    return response.data;
  } catch (error) {
    console.error("An error occurred while getting the project templates: ", error);
  }
};

export const selectTemplate = async (project_id, template) => {
  try {
    console.log("The project id in selectT is:",project_id)
    console.log("The template in selectT is:",template)
    const payload = {
      template_id: template.tid
    }
    console.log("The payload in selectT is:",payload)
    const response = await apiClient.post(`/projects/${project_id}/select-template?template_id=${template.tid}`, payload);
    // console.log("The templates are", response)
    return response.data;
  } catch (error) {
    console.error("An error occurred while getting the project templates: ", error);
  }
};


// Get section by a specific attibute and his value(id, order, name, etc.)
export const getSectionByAttribute = async (attribute, value) => {
  try {
    const response = await apiClient.get(`/sections/by/${attribute}/${value}`);
    return response.data;
  } catch (error) {
    // Gestion des erreurs
    console.error(`An error occurred while fetching the section with ${attribute} ${value}: `, error);
  }
}

export const getNumberOfSections = async () => {
  try {
    // Assume fetchNumberOfSections is a function that fetches the number of sections from the database
    const numberOfSections = await apiClient.get(`/sections`);
    if (numberOfSections !== null && numberOfSections !== undefined) {
      return numberOfSections.lenght;
    } else {
      return 1; // Default to 1 section if no data is returned
    }
  } catch (error) {
    console.error("Failed to fetch the number of sections:", error);
    return 1; // Default to 1 section if an error occurs
  }
};
