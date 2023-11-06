import apiClient from "./api";

export const createTemplate = async (template) => {
  try {
    const response = await apiClient.post("/templates/", template);
    console.log("Create Template", response)
    return response.data;
  } catch (error) {
    // Gestion des erreurs
    console.error("An error occurred while creating the project: ", error);
    return { error: "An error occurred while creating the project." };
  }
};

export const getAllTemplates = async () => {
  try {
    const response = await apiClient.get("/templates/");
    console.log("Get All Templates", response)
    return response.data;
  } catch (error) {
    // Gestion des erreurs
    console.error("An error occurred while fetching the templates: ", error);
    return { error: "An error occurred while fetching the templates." };
  }
};

export const addTemplateForUser = async (username, template) => {
  try {

    const response = await apiClient.post(`/auth/users/${username}/templates`, template);
    console.log("Add Template to User", response)
    return response.data;
  } catch (error) {
    // Gestion des erreurs
    console.error("An error occurred while adding the template to the user: ", error);
    return { error: "An error occurred while adding the template to the user." };
  }
}