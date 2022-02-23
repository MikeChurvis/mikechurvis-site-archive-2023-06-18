export { delayPromise, generateRandomId }

/** 
 * Delays the resolution/rejection of a given promise by a given time. 
 */
function delayPromise<T>(milliseconds: number, promise: Promise<T>): Promise<T> {
  return Promise.all([
    promise,
    new Promise(resolve => setTimeout(resolve, milliseconds)),
  ]).then(([response]) => response);
}

/** 
 * Returns a random 6-digit hexadecimal value. 
 */
function generateRandomId(): string {
  return Math.floor(
    Math.random() * 16777215 // 16777215 = 16^6 - 1
  ).toString(16)
}
