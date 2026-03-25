import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

try:
    size = float(input("Enter circle radius (e.g., 0.05): "))
    speed = float(input("Enter speed (e.g., 0.02): "))
except ValueError:
    print("Invalid input. Using defaults.")
    size, speed = 0.032, 5.2

fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')

ax.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray')
ax.set_title(f"Diagonal Movement | Radius: {size} | Speed: {speed}")

pos = [size + 0.01, size + 0.01]
direction = [1, 1]  # Diagonal vector [dx, dy]

circle = plt.Circle((pos[0], pos[1]), size, color='teal', alpha=0.7)
ax.add_patch(circle)

def update(frame):
    # Update position
    pos[0] += direction[0] * speed
    pos[1] += direction[1] * speed

    # 3. Collision Logic with Grid Boundaries
    # Horizontal bounce
    if pos[0] + size >= 1:
        pos[0] = 1 - size
        direction[0] *= -1
    elif pos[0] - size <= 0:
        pos[0] = size
        direction[0] *= -1
    
    # Vertical bounce
    if pos[1] + size >= 1:
        pos[1] = 1 - size
        direction[1] *= -1
    elif pos[1] - size <= 0:
        pos[1] = size
        direction[1] *= -1

    circle.set_center((pos[0], pos[1]))
    return circle,

ani = FuncAnimation(fig, update, frames=200, interval=20, blit=True, cache_frame_data=False)

plt.show()