import math

def erlang_b(traffic_intensity, num_channels):
    if num_channels == 0:
        return 1
    else:
        e_last = erlang_b(traffic_intensity, num_channels - 1)
        return (traffic_intensity * e_last) / (num_channels + traffic_intensity * e_last)

def max_users(block_prob_threshold, user_traffic_intensity, num_channels):
    total_traffic = 0
    while True:
        total_traffic += user_traffic_intensity
        block_prob = erlang_b(total_traffic, num_channels)
        print(block_prob)
        if block_prob > block_prob_threshold:
            break
    return (total_traffic - user_traffic_intensity) / user_traffic_intensity

num_channels = 30
block_prob_threshold = 0.02
user_traffic_intensity = 0.05*2

max_users_connected = math.floor(max_users(block_prob_threshold, user_traffic_intensity, num_channels))
block_probability = erlang_b(max_users_connected * user_traffic_intensity, num_channels)
total_traffic = max_users_connected * user_traffic_intensity

print(f"Maksymalna liczba użytkowników, którzy mogą być połączeni z Hubem: {max_users_connected}")
print(f"Prawdopodobieństwo blokady: {block_probability:.2%}")
print(f"Całkowity ruch generowany przez maksymalną liczbę użytkowników: {total_traffic:.2f} Erlang")
