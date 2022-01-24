import { delayPromise } from "@/scripts/main";


export type MessageData = {
    name: String;
    company: String;
    email: String;
    content: String;
}

export type MessageDataValidator = (messageData: MessageData) => MessageDataValidatorResponse;

export type MessageDataValidatorResponse = {
    valid: Boolean;
    errors?: {
        name?: String;
        company?: String;
        email?: String;
        content?: String;
    };
}

export type MessagePostFunction = (messageData: MessageData) => Promise<Response>;

export enum FormState {
    ReadyForInput,
    AwaitingServerResponse,
    Success,
}


type DebugObject = {
    delay?: number,
    responsePayload?: string,
}

export function postContactFormDataFactory(targetUrl: string, debug: DebugObject = {}): MessagePostFunction {
    const isDebugMode = Object.keys(debug).length > 0;

    let postFunction: MessagePostFunction;

    if (isDebugMode) {
        
        postFunction = async (messageData: MessageData) => {
            console.log(debug);
            const delay = debug.delay ?? 0;
            const responsePayload = JSON.parse(debug.responsePayload ?? "{}")

            const payload = responsePayload ?? {
                debug: true,
                delay: delay,
                requestData: messageData,
            };

            const response = new Response(
                new Blob(
                    [JSON.stringify(payload)],
                    { type: 'application/json' }
                ),
                { status: 200, statusText: "ok" },
            );

            return delayPromise(delay, Promise.resolve(response));
        };

    } else {
        postFunction = async (messageData: MessageData) => fetch(targetUrl, {
            method: "POST",
            headers: {
                "Access-Control-Allow-Origin": origin,
            },
            credentials: "same-origin",
            body: JSON.stringify(messageData),
        });
    }

    return postFunction;
}