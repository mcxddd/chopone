export interface Message {
  type: "user" | "ai" | "error" | "loading" | "system";
  content: string;
}
