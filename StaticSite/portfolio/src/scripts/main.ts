export function delayPromise<T> (milliseconds: number, promise: Promise<T>): Promise<T> {
    return Promise.all([
        promise,
        new Promise(resolve => setTimeout(resolve, milliseconds)),
    ]).then(([response]) => response);
}


export enum InputType {
    Text = 'text',
    Email = 'email',
    TextArea = 'textarea',
}