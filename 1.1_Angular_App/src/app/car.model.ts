export interface Car {
    id: string;
    name: string;
    brand: string;
    services: Service[];
}


export interface Service {
    id: string;
    name: string;
    date: string;
    cost: number;
}
