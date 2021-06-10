import pygame


class Card:
    def __init__(self, head_1, head_2, img, *vars):
        pygame.init()
        self.font = pygame.font.SysFont('courier header', 32)
        self.head_1 = head_1.split('\n')
        self.head_2 = head_2.split('\n')
        self.img = pygame.transform.scale(pygame.image.load(img), self.transform_img(img))
        self.answers = vars
        self.size = (55 + 15 * max(
            [len(i) for i in self.head_1] + [len(i) for i in self.head_2] + [len(i) for i in self.answers] + [
                self.img.get_size()[0] // 15]),
                     15 + 30 * len(self.head_1) + 30 + self.img.get_size()[1] + 35 * len(self.head_2) + 60 + 30 * len(
                         self.answers) + 15 * (len(self.answers) - 1) + 15)
        self.display = pygame.display.set_mode(self.size)

    def transform_img(self, img):
        img = pygame.image.load(img)
        key = 1
        while img.get_size()[0] // key > 300 or img.get_size()[1] // key > 300:
            key += 1
        return img.get_size()[0] // key, img.get_size()[1] // key

    def print_phrases_and_img(self):
        for i in range(len(self.head_1)):
            text = self.font.render(self.head_1[i], False, (0, 255, 0))
            text_rect = text.get_rect(center=(self.size[0] // 2, 30 + (50 * i // 2)))
            self.display.blit(text, text_rect)

        rect = self.img.get_rect(
            center=(self.size[0] // 2, 30 + (50 * len(self.head_1) // 2) + self.img.get_size()[1] // 2))

        self.display.blit(self.img, rect)
        for i in range(len(self.head_2)):
            text = self.font.render(self.head_2[i], False, (0, 255, 0))
            text_rect = text.get_rect(
                center=(self.size[0] // 2, 30 + (50 * len(self.head_1) // 2) + self.img.get_size()[1] + 30 + 30 * i))
            self.display.blit(text, text_rect)

    def print_answer_options(self):
        height = 30 * len(self.answers) + 15 * (len(self.answers) - 1)

        pygame.draw.lines(self.display, 'green', False, [[30, self.size[1] - 30],
                                                         [15, self.size[1] - 30],
                                                         [15, self.size[1] - 30 - height],
                                                         [30, self.size[1] - 30 - height]])

        pygame.draw.lines(self.display, 'green', False, [[self.size[0] - 30, self.size[1] - 30],
                                                         [self.size[0] - 15, self.size[1] - 30],
                                                         [self.size[0] - 15, self.size[1] - 30 - height],
                                                         [self.size[0] - 30, self.size[1] - 30 - height]])

        for i in range(len(self.answers)):
            pygame.draw.lines(self.display, 'green', False, [[40, self.size[1] - 30 + 45 * i - height + 5],
                                                             [55, self.size[1] - 15 + 45 * i - height],
                                                             [40, self.size[1] + 45 * i - height - 5]], 2)
            self.display.blit(self.font.render(self.answers[i], False, (0, 255, 0)),
                              [60, self.size[1] - 30 + 45 * i - height + 5])

    def show(self):
        pygame.draw.rect(self.display, 'green', (5, 5, self.size[0] - 10, self.size[1] - 10), 3)
        self.print_phrases_and_img()
        self.print_answer_options()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            pygame.display.update()


if __name__ == '__main__':
    first_head = 'МАЛЕНЬКИЙ КРАБ медленно подошел. \nОн выглядит очень грустным...'
    second_head = '"Позволь мне уйти", - просит он. \n "Я так давно не видел мою семью."'
    img = 'current_img.jpg'
    answers = ['ОТПУСТИТЬ МАЛЕНЬКОГО КРАБА', '"Тебе ещё нужно ДОПИСАТЬ ОТЧЁТ"', 'ГЛУМИТЬСЯ над МАЛЕНЬКИМ КРАБОМ', 'Просто смотреть']

    example = Card(first_head, second_head, img, *answers)
    example.show()
