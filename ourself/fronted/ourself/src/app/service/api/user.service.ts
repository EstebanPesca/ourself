import { Injectable } from '@angular/core';
import { LoginI } from '../../models/login/login.interface';
import { HttpClient } from '@angular/common/http';
import { catchError, throwError } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  public accessToken: string = '';

  private urlApi:string = "http://127.0.0.1:8000/auth/";

  constructor( private http:HttpClient) { }

  login(form:LoginI){
    return this.http.post<any>(`${this.urlApi}login/`, form).pipe(
      catchError((error) => {
        if(error.status === 401){
          return throwError('Invalid credentials.');
        }else{
          return throwError('An unexpected error ocurred.');
        }
      })
    )
  }

  setAccessToken(token:string){
    localStorage.setItem('token',token);
  }

  getAccessToken(){
    return localStorage.getItem('token');
  }

  isLogged(){
    return this.getAccessToken();
  }

}
