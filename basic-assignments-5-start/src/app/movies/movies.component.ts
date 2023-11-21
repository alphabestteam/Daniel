import { Component, OnInit } from '@angular/core';
import { StarWarsMovie } from '../star-wars-movie';
import { FILMS } from '../star-wars-fake-db/film-data';

@Component({
  selector: 'app-movies',
  templateUrl: './movies.component.html',
  styleUrls: ['./movies.component.scss']
})
export class MoviesComponent {
  movies: StarWarsMovie[] = FILMS;
}
