export interface Toast {
  id: number;
  message: string;
  type: "success" | "error";
  duration: number;
}