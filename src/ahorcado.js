let secretWord = '';
let masked = undefined;
let state = '';

export function setSecretWord(word){
  secretWord = String(word ?? '');
  state = 'EN_CURSO';
  masked = '_'.repeat(secretWord.length);
}

// Todavía sin implementar
export function getMaskedWord() {
  return undefined; // intencional
}

// Todavía sin implementar
export function getState() {
  return gameState;
}
