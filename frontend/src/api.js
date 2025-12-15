import axios from 'axios';

const API_URL = '/api';

export const searchAnalysis = async (query, filters) => {
  try {
    const response = await axios.post(`${API_URL}/analyze`, { query, filters });
    return response.data;
  } catch (error) {
    console.error("Error fetching analysis:", error);
    throw error;
  }
};

export const generateReport = async (query, filters) => {
  try {
    const response = await axios.post(`${API_URL}/report`, { query, filters }, { responseType: 'blob' });
    const url = window.URL.createObjectURL(new Blob([response.data]));
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', 'report.pdf');
    document.body.appendChild(link);
    link.click();
    link.remove();
  } catch (error) {
    console.error("Error generating report:", error);
    throw error;
  }
};
