import pygame

class GameLoop:
    def __init__(self, renderer, event_queue, clock, board):
        self._clock = clock
        self._renderer = renderer
        self._event_queue = event_queue
        self._board = board

    def start(self):

        turned = []
        matched = 0

        while True:
            if self._handle_events(turned, matched) == False:
                break

            self._render()

            if matched == 18:
                print('Victory!')

            if len(turned) >= 2:
                if self._board.cards[turned[0]].get_id() == self._board.cards[turned[1]].get_id():
                    print('Match!')
                    self._board.cards[turned[0]].set_match()
                    self._board.cards[turned[1]].set_match()
                    matched+=2
                    turned.clear()
                else:
                    pygame.time.wait(1500)
                    for i in range(2):
                        self._board.cards[turned[i]].turn_over()
                    turned.clear()

            self._clock.tick(60)

    def _handle_events(self, turned, matched):
        self.turned = turned
        self.matched = matched
        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                k=0
                for card in self._board.cards:
                    if card.get_location().collidepoint(mouse_pos):
                        
                        print('Clicked on ' + str(card.get_id()))
                        card.turn_over()
                        turned.append(k)
                    k+=1


    def _render(self):
        self._renderer.render()
