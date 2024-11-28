import { Component } from '@angular/core';
import { LocalStorageService } from '../local-storage.service';
import { Car } from '../car.model';

@Component({
  selector: 'app-cars',
  templateUrl: './cars.component.html',
  styleUrl: './cars.component.css'
})
export class CarsComponent {
  cars: Car[] = [];

  constructor(private localStorageService: LocalStorageService) {}
  addCar() {
    const newCar: Car = {
      id: Date.now().toString(),
      name: 'Nowy samochód',
      brand: 'Nieznana marka',
      services: []
    };
    this.cars.push(newCar);
    this.localStorageService.saveData('cars', this.cars);

  }

  loadCars() {
    this.cars = this.localStorageService.getData('cars') || [];
  }
}
