from datetime import datetime
import pygame

class GameLoop:
    """Luokka, jonka vastulla on game loopin ylläpitäminen ja pelaajan syötteiden käsitteleminen.

    Attributes:
        _clock: Clock olio, jonka vastuulla on pelin ajoittaminen
        _renderer: Renderer-olio,
                 jonka vastuulla on eri elementtien piirtäminen ruudulle
        _event_queue: EventQueue-olio,
                 jonka vastuulla on tapahtumien käsittely. Esim. pelaajan syötteet
        _board: Board-olio, jonka vastuulla on peliruudukon luominen
        _turned: Taulukko, joka pitää yllä käännetyt kortit
        _matched: Kokonaislukumuuttuja, joka kuvaa, kuinka monta korttiparia on löydetty
        turns: Kokonaislukumuuttuja, joka kuvaa, kuinka monta kierrosta on pelattu
        mistakes: Kokonaislukumuuttuja, joka kuvaa, kuinka monta virhettä pelaaja on tehnyt
        _seen: Set-tietorakenne, joka muistaa mitkä kortit on jo aikaisemmin nähty
    """
    def __init__(self, renderer, event_queue, clock, board):
        """Luokan konstruktori, joka luo uuden GameLoop-olion

        Args:
            renderer (Renderer): Renderer-olio,
                             jonka vastuulla on eri elementtien piirtäminen ruudulle
            event_queue (EventQueue): EventQueue-olio, jonka vastuulla on tapahtumien käsittely
            clock (Clock): Clock-olio, jonka vastuulla on pelin ajoitusten hoitaminen
            board (Board): Board-olio, jonka vastuulla on peliruudukon luominen
        """
        self._clock = clock
        self._renderer = renderer
        self._event_queue = event_queue
        self._board = board
        self._turned = []
        self._matched = 0
        self.turns = 0
        self.mistakes = 0
        self._seen = set()
        self._game_over = False

    def start(self):
        """Aloittaa game loopin ja tarkastaa 60 kertaa sekunnissa pelin tilan
        """
        while True:
            if self._handle_events() is False or self._game_over is True:
                break

            self._render()

            if self._matched == self._board.rows * self._board.columns:
                pygame.time.wait(300)
                self._renderer.render_go_screen(self.turns, self.mistakes,
                                                 self._clock.get_ticks()/1000)
                save_score = open("scores.txt", "a")
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                save_score.write("Date: " + dt_string + ", Turns: " + str(self.turns) + \
                                ", Mistakes: " + str(self.mistakes) + "\n")
                while True:
                    if self._handle_events() is False:
                        self._game_over = True
                        break

            if len(self._turned) >= 2:
                if self._turned[0].get_id() == self._turned[1].get_id():
                    self._turned[0].set_match()
                    self._turned[1].set_match()
                    self._matched += 2
                else:
                    pygame.time.wait(1300)
                    for i in range(2):
                        self._turned[i].turn_over()
                    if self._turned[0].get_id() in self._seen:
                        self.mistakes += 1
                self._seen.add(self._turned[0].get_id())
                self._seen.add(self._turned[1].get_id())
                self._turned.clear()
                self.turns += 1

            self._clock.tick(60)

    def _handle_events(self):
        """Tapahtumankäsitteljä, joka hoitaa pelaajan syötteiden käsittelyn

        Returns:
            Boolean: Palauttaa False, jos pelaaja on sulkenut ohjelman.
                    Muussa tapauksessa palauttaa True
        """
        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for card in self._board.cards:
                    if card.get_location().collidepoint(mouse_pos):
                        #The prints/elifs are there for future purposes,
                        #for example the cards could jiggle a bit if
                        #already turned/matched
                        if card.get_matched() is True:
                            print("Already matched: do nothing")
                        elif card.get_turned_over() is True:
                            print("Already turned over: do nothing")
                        else:
                            card.turn_over()
                            self._turned.append(card)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return False
        return True

    def _render(self):
        """Piirtää uuden pelitilan ruudulle
        """
        self._renderer.render_board(self.turns, self.mistakes, self._clock.get_ticks()/1000)
    