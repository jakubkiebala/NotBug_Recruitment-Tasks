import { Component, Input, OnInit } from '@angular/core';
import { LocalStorageService } from '../local-storage.service';  // Poprawny import
import { Car, Service } from '../car.model';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';  // Dodaj FormsModule

@Component({
  selector: 'app-services',
  templateUrl: './services.component.html',
  styleUrls: ['./services.component.css'],
  imports: [CommonModule, FormsModule]  // Importujemy FormsModule
})
export class ServicesComponent implements OnInit {
  @Input() carId: string = '';  // Odbieramy ID samochodu z zewnątrz
  car: Car | null = null;
  newService: Service = {
    id: '',
    name: '',
    date: '',
    cost: 0,
  };

  constructor(private localStorageService: LocalStorageService) {}

  ngOnInit() {
    this.loadCar();  // Załaduj samochód na początku
  }

  // Ładujemy dane samochodu z localStorage
  loadCar() {
    const cars: Car[] = this.localStorageService.getData('cars') || [];
    this.car = cars.find((c) => c.id === this.carId) || null;
  }

  // Dodajemy nowy serwis
  addService() {
    if (!this.car) return;

    const service: Service = {
      ...this.newService,
      id: Date.now().toString(),  // Generujemy unikalny ID
    };

    this.car.services.push(service);  // Dodajemy serwis do samochodu

    const cars: Car[] = this.localStorageService.getData('cars') || [];
    const carIndex = cars.findIndex((c) => c.id === this.carId);

    if (carIndex !== -1) {
      cars[carIndex] = this.car;  // Zapisujemy zmodyfikowany samochód
      this.localStorageService.saveData('cars', cars);  // Zapisujemy zaktualizowane dane do localStorage
    }

    // Resetowanie formularza po dodaniu serwisu
    this.newService = {
      id: '',
      name: '',
      date: '',
      cost: 0,
    };
  }
}


