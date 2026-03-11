
import input from './input.json';
import results from './results.json';

const meta = {
  id: 'taucp-ml',
  name: 'TauCP Machine Learning',
  description: 'Transformer-based machine learning model for TauCP tasks',
};

const subpages = [
  input,
  results,
];

export default {
  ...meta,
  subpages,
};
