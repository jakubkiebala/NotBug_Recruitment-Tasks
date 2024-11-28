import { Component, OnInit } from '@angular/core';
import { LocalStorageService } from '../local-storage.service'; // Poprawny import
import { CommonModule } from '@angular/common';  // Dodatkowo potrzebujemy CommonModule, jeśli używamy *ngFor
import { FormsModule } from '@angular/forms';  // Importujemy FormsModule

@Component({
  selector: 'app-cars',
  templateUrl: './cars.component.html',
  styleUrls: ['./cars.component.css'],
  imports: [CommonModule, FormsModule],  // Importujemy FormsModule
  providers: [LocalStorageService] // Rejestrujemy serwis w tym komponencie
})
export class CarsComponent implements OnInit {
  cars: any[] = [];
  
  // Nowy samochód, który będziemy dodawać
  newCar = {
    id: '',
    name: '',
    brand: '',
    services: []
  };

  constructor(private localStorageService: LocalStorageService) {}

  ngOnInit() {
    this.loadCars();
  }

  loadCars() {
    this.cars = this.localStorageService.getData('cars') || [];
  }

  addCar() {
    if (!this.newCar.name || !this.newCar.brand) {
      return; // Jeśli nie wprowadzono nazwy lub marki, nie dodajemy samochodu
    }

    const newCar = {
      ...this.newCar,
      id: Date.now().toString(),  // Generujemy unikalny ID
    };

    this.cars.push(newCar);
    this.localStorageService.saveData('cars', this.cars);

    // Resetujemy formularz po dodaniu samochodu
    this.newCar = {
      id: '',
      name: '',
      brand: '',
      services: []
    };
  }
}

