import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'  // Serwis dostępny w całej aplikacji
})
export class LocalStorageService {
  getData(key: string): any {
    if (typeof window !== 'undefined' && window.localStorage) {
      const data = localStorage.getItem(key);
      return data ? JSON.parse(data) : null;
    }
    return null; // Zwróć null lub pustą wartość, gdy nie jest dostępny localStorage
  }

  saveData(key: string, data: any): void {
    if (typeof window !== 'undefined' && window.localStorage) {
      localStorage.setItem(key, JSON.stringify(data));
    }
  }
}
