import test from 'node:test';
import assert from 'node:assert/strict';
import { setSecretWord, getMaskedWord, getState } from './ahorcado.js';

test('Funcionalidad 1 - Establecer palabra', () => {

  const palabra = 'CASA';
  
  setSecretWord(palabra);

  assert.ok(getMaskedWord() !== undefined, 'La máscara debe existir');
  assert.strictEqual(getState(), 'EN_CURSO');

test('Funcionalidad 2 - La máscara tiene tantos guiones como letras', () => {
  const palabra = 'CASA';
  setSecretWord(palabra);


  const masked = getMaskedWord();

  assert.strictEqual(masked.length, palabra.length, 'La máscara debe tener la misma longitud que la palabra');
  assert.match(masked, /^_+$/, 'La máscara debe estar compuesta solo de guiones bajos');
});
});
