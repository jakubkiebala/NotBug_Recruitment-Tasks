import { Component, OnInit } from '@angular/core';
import { LocalStorageService } from '../local-storage.service'; // Importujemy serwis
import { CommonModule } from '@angular/common';  // Jeśli używasz *ngFor, dodaj CommonModule

@Component({
  selector: 'app-cars',
  templateUrl: './cars.component.html',
  styleUrls: ['./cars.component.css'],
  imports: [CommonModule]  // Dodaj CommonModule, jeśli używasz *ngFor w szablonie
})
export class CarsComponent implements OnInit {
  cars: { id: string; name: string; brand: string; services: any[] }[] = []; // Definiowanie typu dla samochodów

  constructor(private localStorageService: LocalStorageService) {}

  ngOnInit() {
    this.loadCars();
  }

  loadCars() {
    this.cars = this.localStorageService.getData('cars') || [];
  }

  addCar() {
    const newCar = {
      id: Date.now().toString(),
      name: 'Nowy samochód',
      brand: 'Nieznana marka',
      services: []
    };
    this.cars.push(newCar);
    this.localStorageService.saveData('cars', this.cars);
  }
}
