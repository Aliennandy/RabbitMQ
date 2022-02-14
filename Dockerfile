FROM rabbitmq:3.8-management
RUN rabbitmq-plugins enable --offline rabbitmq_mqtt rabbitmq_web_mqtt 

EXPOSE 1883
EXPOSE 15675
EXPOSE 15672
EXPOSE 5671
EXPOSE 5672 

networks:
  rabbitmq_go_net:
    driver: bridge
