import { Injectable } from "@angular/core";

@Injectable({
    providedIn: 'root',
})
export class LocalStorageService {
    saveData(key: string, value: any): void {
        localStorage.setItem(key, JSON.stringify(value));
    }

    getData(key: string): any {
        const data = localStorage.getItem(key);
        return data ? JSON.parse(data) : null;
    }
}

