import test from 'node:test';
import assert from 'node:assert/strict';
import { setSecretWord, getMaskedWord, getState } from './ahorcado.js';

test('Funcionalidad 1 - Establecer palabra', () => {

  const palabra = 'CASA';

  setSecretWord(palabra);

  assert.ok(getMaskedWord() !== undefined, 'La máscara debe existir');
  assert.strictEqual(getState(), 'EN_CURSO');
});
