import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, Button
import random
import math


class SimpleDartTarget:
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(8, 8))
        plt.subplots_adjust(bottom=0.2)

        self.radii = [math.sqrt(0.1), math.sqrt(0.4), math.sqrt(1.0)]
        self.probabilities = [0.1, 0.3, 0.6]
        self.colors = ['red', 'blue', 'green']
        self.zone_names = ['Малый', 'Средний', 'Большой']

        self.total_throws = 0
        self.hits = [0, 0, 0]

        self.setup_plot()
        self.setup_widgets()

    def setup_plot(self):
        max_radius = self.radii[2]
        self.ax.set_xlim(-max_radius * 1.2, max_radius * 1.2)
        self.ax.set_ylim(-max_radius * 1.2, max_radius * 1.2)
        self.ax.set_aspect('equal')
        self.ax.set_xticks([])
        self.ax.set_yticks([])

        for i, radius in enumerate(self.radii):
            circle = plt.Circle((0, 0), radius, color=self.colors[i],
                                alpha=0.3, ec='black', linewidth=2)
            self.ax.add_patch(circle)
            self.ax.text(0, radius + 0.05, f'{self.probabilities[i] * 100}%',
                         ha='center', fontsize=10, weight='bold')

        self.stats_text = self.ax.text(-max_radius * 1.1, -max_radius * 1.1, self.get_stats_text(),
                                       fontsize=10, bbox=dict(boxstyle="round", facecolor="lightgray"))

    def setup_widgets(self):
        ax_textbox = plt.axes([0.2, 0.05, 0.15, 0.05])
        self.throw_textbox = TextBox(ax_textbox, 'Бросков:', initial='100')

        ax_throw = plt.axes([0.4, 0.05, 0.15, 0.05])
        self.throw_button = Button(ax_throw, 'Бросить!')
        self.throw_button.on_clicked(self.throw_darts)

        ax_reset = plt.axes([0.6, 0.05, 0.15, 0.05])
        self.reset_button = Button(ax_reset, 'Сбросить')
        self.reset_button.on_clicked(self.reset_all)

    def get_stats_text(self):
        text = f"Бросков: {self.total_throws}\n"
        if self.total_throws > 0:
            for i, hit_count in enumerate(self.hits):
                percentage = (hit_count / self.total_throws) * 100
                text += f"{self.zone_names[i]}: {hit_count} ({percentage:.1f}%)\n"
        else:
            for zone in self.zone_names:
                text += f"{zone}: 0 (0.0%)\n"
        return text

    def throw_darts(self, event):
        try:
            num_throws = int(self.throw_textbox.text)
            if num_throws <= 0:
                return
        except ValueError:
            return

        max_radius = self.radii[2]

        for _ in range(num_throws):
            angle = random.uniform(0, 2 * np.pi)
            radius_point = max_radius * math.sqrt(random.uniform(0, 1))

            x = radius_point * math.cos(angle)
            y = radius_point * math.sin(angle)
            distance = math.sqrt(x ** 2 + y ** 2)

            zone = None
            for i, radius in enumerate(self.radii):
                if distance <= radius:
                    zone = i
                    break

            if zone is not None:
                self.hits[zone] += 1
                self.ax.plot(x, y, 'o', markersize=4,
                             color='black', alpha=0.7)

        self.total_throws += num_throws
        self.stats_text.set_text(self.get_stats_text())
        self.fig.canvas.draw_idle()

    def reset_all(self, event):
        self.total_throws = 0
        self.hits = [0, 0, 0]

        max_radius = self.radii[2]
        self.ax.clear()
        self.ax.set_xlim(-max_radius * 1.2, max_radius * 1.2)
        self.ax.set_ylim(-max_radius * 1.2, max_radius * 1.2)
        self.ax.set_aspect('equal')
        self.ax.set_xticks([])
        self.ax.set_yticks([])

        for i, radius in enumerate(self.radii):
            circle = plt.Circle((0, 0), radius, color=self.colors[i],
                                alpha=0.3, ec='black', linewidth=2)
            self.ax.add_patch(circle)
            self.ax.text(0, radius + 0.05, f'{self.probabilities[i] * 100}%',
                         ha='center', fontsize=10, weight='bold')

        self.stats_text = self.ax.text(-max_radius * 1.1, -max_radius * 1.1, self.get_stats_text(),
                                       fontsize=10, bbox=dict(boxstyle="round", facecolor="lightgray"))

        self.fig.canvas.draw_idle()


if __name__ == "__main__":
    target = SimpleDartTarget()
    plt.show()