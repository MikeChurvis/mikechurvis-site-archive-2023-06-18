/// <reference types="vite/client" />

interface ImportMetaEnv {
    readonly PUBLIC_CONTACT_FORM_TARGET: string;
}

interface ImportMeta {
    readonly env: ImportMetaEnv;
}