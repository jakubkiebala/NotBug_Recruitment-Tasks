import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',  // Serwis dostępny globalnie w aplikacji
})
export class LocalStorageService {
  getData(key: string): any {
    if (typeof window !== 'undefined' && window.localStorage) {
      const data = localStorage.getItem(key);
      return data ? JSON.parse(data) : null;
    }
    return null; // Zwróć null, gdy localStorage nie jest dostępny
  }

  saveData(key: string, data: any): void {
    if (typeof window !== 'undefined' && window.localStorage) {
      localStorage.setItem(key, JSON.stringify(data));
    }
  }
}
