import pygame


class GameLoop:
    def __init__(self, renderer, event_queue, clock, board):
        self._clock = clock
        self._renderer = renderer
        self._event_queue = event_queue
        self._board = board
        self._turned = []
        self._matched = 0

    def start(self):

        turns = 0
        mistakes = 0

        while True:
            if self._handle_events() is False:
                break

            self._render()

            if self._matched == self._board.rows * self._board.columns:
                print('Victory!')

            if len(self._turned) >= 2:
                if self._turned[0].get_id() == self._turned[1].get_id():
                    print("Match!")
                    self._turned[0].set_match()
                    self._turned[1].set_match()
                    self._matched += 2
                else:
                    pygame.time.wait(1300)
                    for i in range(2):
                        self._turned[i].turn_over()
                    mistakes += 1
                self._turned.clear()
                turns += 1

            self._clock.tick(60)

    def _handle_events(self):
        #self.turned = turned
        #self.matched = matched
        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for card in self._board.cards:
                    if card.get_location().collidepoint(mouse_pos):

                        print('Clicked on ' + str(card.get_id()))
                        if card.get_matched() is True:
                            print("Already matched: do nothing")
                        elif card.get_turned_over() is True:
                            print("Already turned over: do nothing")
                        else:
                            card.turn_over()
                            self._turned.append(card)
        return True

    def _render(self):
        self._renderer.render()
