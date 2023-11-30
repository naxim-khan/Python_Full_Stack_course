
#     count_min=math.floor(count/60)
#     count_sec=count%60
#     if count_sec < 10:
#         count_sec=f"0{count_sec}"

#     canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
#     timer_label.config(text=f"{count_min}:{count_sec}")

#     if count>0:
#         window.after(1000,count_down,count-1)
#     else:
#         start_timer()