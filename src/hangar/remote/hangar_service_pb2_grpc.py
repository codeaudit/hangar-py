# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import hangar_service_pb2 as hangar__service__pb2


class HangarServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.FetchBranchRecord = channel.unary_unary(
        '/hangar.HangarService/FetchBranchRecord',
        request_serializer=hangar__service__pb2.FetchBranchRecordRequest.SerializeToString,
        response_deserializer=hangar__service__pb2.FetchBranchRecordReply.FromString,
        )
    self.FetchData = channel.stream_stream(
        '/hangar.HangarService/FetchData',
        request_serializer=hangar__service__pb2.FetchDataRequest.SerializeToString,
        response_deserializer=hangar__service__pb2.FetchDataReply.FromString,
        )
    self.FetchLabel = channel.unary_unary(
        '/hangar.HangarService/FetchLabel',
        request_serializer=hangar__service__pb2.FetchLabelRequest.SerializeToString,
        response_deserializer=hangar__service__pb2.FetchLabelReply.FromString,
        )
    self.FetchCommit = channel.unary_stream(
        '/hangar.HangarService/FetchCommit',
        request_serializer=hangar__service__pb2.FetchCommitRequest.SerializeToString,
        response_deserializer=hangar__service__pb2.FetchCommitReply.FromString,
        )
    self.FetchSchema = channel.unary_unary(
        '/hangar.HangarService/FetchSchema',
        request_serializer=hangar__service__pb2.FetchSchemaRequest.SerializeToString,
        response_deserializer=hangar__service__pb2.FetchSchemaReply.FromString,
        )
    self.PushBranchRecord = channel.unary_unary(
        '/hangar.HangarService/PushBranchRecord',
        request_serializer=hangar__service__pb2.PushBranchRecordRequest.SerializeToString,
        response_deserializer=hangar__service__pb2.PushBranchRecordReply.FromString,
        )
    self.PushData = channel.stream_unary(
        '/hangar.HangarService/PushData',
        request_serializer=hangar__service__pb2.PushDataRequest.SerializeToString,
        response_deserializer=hangar__service__pb2.PushDataReply.FromString,
        )
    self.PushLabel = channel.unary_unary(
        '/hangar.HangarService/PushLabel',
        request_serializer=hangar__service__pb2.PushLabelRequest.SerializeToString,
        response_deserializer=hangar__service__pb2.PushLabelReply.FromString,
        )
    self.PushCommit = channel.stream_unary(
        '/hangar.HangarService/PushCommit',
        request_serializer=hangar__service__pb2.PushCommitRequest.SerializeToString,
        response_deserializer=hangar__service__pb2.PushCommitReply.FromString,
        )
    self.PushSchema = channel.unary_unary(
        '/hangar.HangarService/PushSchema',
        request_serializer=hangar__service__pb2.PushSchemaRequest.SerializeToString,
        response_deserializer=hangar__service__pb2.PushSchemaReply.FromString,
        )
    self.FetchFindMissingCommits = channel.unary_unary(
        '/hangar.HangarService/FetchFindMissingCommits',
        request_serializer=hangar__service__pb2.FindMissingCommitsRequest.SerializeToString,
        response_deserializer=hangar__service__pb2.FindMissingCommitsReply.FromString,
        )
    self.FetchFindMissingHashRecords = channel.stream_stream(
        '/hangar.HangarService/FetchFindMissingHashRecords',
        request_serializer=hangar__service__pb2.FindMissingHashRecordsRequest.SerializeToString,
        response_deserializer=hangar__service__pb2.FindMissingHashRecordsReply.FromString,
        )
    self.FetchFindMissingLabels = channel.stream_stream(
        '/hangar.HangarService/FetchFindMissingLabels',
        request_serializer=hangar__service__pb2.FindMissingLabelsRequest.SerializeToString,
        response_deserializer=hangar__service__pb2.FindMissingLabelsReply.FromString,
        )
    self.FetchFindMissingSchemas = channel.unary_unary(
        '/hangar.HangarService/FetchFindMissingSchemas',
        request_serializer=hangar__service__pb2.FindMissingSchemasRequest.SerializeToString,
        response_deserializer=hangar__service__pb2.FindMissingSchemasReply.FromString,
        )
    self.PushFindMissingCommits = channel.unary_unary(
        '/hangar.HangarService/PushFindMissingCommits',
        request_serializer=hangar__service__pb2.FindMissingCommitsRequest.SerializeToString,
        response_deserializer=hangar__service__pb2.FindMissingCommitsReply.FromString,
        )
    self.PushFindMissingHashRecords = channel.stream_stream(
        '/hangar.HangarService/PushFindMissingHashRecords',
        request_serializer=hangar__service__pb2.FindMissingHashRecordsRequest.SerializeToString,
        response_deserializer=hangar__service__pb2.FindMissingHashRecordsReply.FromString,
        )
    self.PushFindMissingLabels = channel.stream_stream(
        '/hangar.HangarService/PushFindMissingLabels',
        request_serializer=hangar__service__pb2.FindMissingLabelsRequest.SerializeToString,
        response_deserializer=hangar__service__pb2.FindMissingLabelsReply.FromString,
        )
    self.PushFindMissingSchemas = channel.unary_unary(
        '/hangar.HangarService/PushFindMissingSchemas',
        request_serializer=hangar__service__pb2.FindMissingSchemasRequest.SerializeToString,
        response_deserializer=hangar__service__pb2.FindMissingSchemasReply.FromString,
        )


class HangarServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def FetchBranchRecord(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FetchData(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FetchLabel(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FetchCommit(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FetchSchema(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PushBranchRecord(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PushData(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PushLabel(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PushCommit(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PushSchema(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FetchFindMissingCommits(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FetchFindMissingHashRecords(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FetchFindMissingLabels(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FetchFindMissingSchemas(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PushFindMissingCommits(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PushFindMissingHashRecords(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PushFindMissingLabels(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PushFindMissingSchemas(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_HangarServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'FetchBranchRecord': grpc.unary_unary_rpc_method_handler(
          servicer.FetchBranchRecord,
          request_deserializer=hangar__service__pb2.FetchBranchRecordRequest.FromString,
          response_serializer=hangar__service__pb2.FetchBranchRecordReply.SerializeToString,
      ),
      'FetchData': grpc.stream_stream_rpc_method_handler(
          servicer.FetchData,
          request_deserializer=hangar__service__pb2.FetchDataRequest.FromString,
          response_serializer=hangar__service__pb2.FetchDataReply.SerializeToString,
      ),
      'FetchLabel': grpc.unary_unary_rpc_method_handler(
          servicer.FetchLabel,
          request_deserializer=hangar__service__pb2.FetchLabelRequest.FromString,
          response_serializer=hangar__service__pb2.FetchLabelReply.SerializeToString,
      ),
      'FetchCommit': grpc.unary_stream_rpc_method_handler(
          servicer.FetchCommit,
          request_deserializer=hangar__service__pb2.FetchCommitRequest.FromString,
          response_serializer=hangar__service__pb2.FetchCommitReply.SerializeToString,
      ),
      'FetchSchema': grpc.unary_unary_rpc_method_handler(
          servicer.FetchSchema,
          request_deserializer=hangar__service__pb2.FetchSchemaRequest.FromString,
          response_serializer=hangar__service__pb2.FetchSchemaReply.SerializeToString,
      ),
      'PushBranchRecord': grpc.unary_unary_rpc_method_handler(
          servicer.PushBranchRecord,
          request_deserializer=hangar__service__pb2.PushBranchRecordRequest.FromString,
          response_serializer=hangar__service__pb2.PushBranchRecordReply.SerializeToString,
      ),
      'PushData': grpc.stream_unary_rpc_method_handler(
          servicer.PushData,
          request_deserializer=hangar__service__pb2.PushDataRequest.FromString,
          response_serializer=hangar__service__pb2.PushDataReply.SerializeToString,
      ),
      'PushLabel': grpc.unary_unary_rpc_method_handler(
          servicer.PushLabel,
          request_deserializer=hangar__service__pb2.PushLabelRequest.FromString,
          response_serializer=hangar__service__pb2.PushLabelReply.SerializeToString,
      ),
      'PushCommit': grpc.stream_unary_rpc_method_handler(
          servicer.PushCommit,
          request_deserializer=hangar__service__pb2.PushCommitRequest.FromString,
          response_serializer=hangar__service__pb2.PushCommitReply.SerializeToString,
      ),
      'PushSchema': grpc.unary_unary_rpc_method_handler(
          servicer.PushSchema,
          request_deserializer=hangar__service__pb2.PushSchemaRequest.FromString,
          response_serializer=hangar__service__pb2.PushSchemaReply.SerializeToString,
      ),
      'FetchFindMissingCommits': grpc.unary_unary_rpc_method_handler(
          servicer.FetchFindMissingCommits,
          request_deserializer=hangar__service__pb2.FindMissingCommitsRequest.FromString,
          response_serializer=hangar__service__pb2.FindMissingCommitsReply.SerializeToString,
      ),
      'FetchFindMissingHashRecords': grpc.stream_stream_rpc_method_handler(
          servicer.FetchFindMissingHashRecords,
          request_deserializer=hangar__service__pb2.FindMissingHashRecordsRequest.FromString,
          response_serializer=hangar__service__pb2.FindMissingHashRecordsReply.SerializeToString,
      ),
      'FetchFindMissingLabels': grpc.stream_stream_rpc_method_handler(
          servicer.FetchFindMissingLabels,
          request_deserializer=hangar__service__pb2.FindMissingLabelsRequest.FromString,
          response_serializer=hangar__service__pb2.FindMissingLabelsReply.SerializeToString,
      ),
      'FetchFindMissingSchemas': grpc.unary_unary_rpc_method_handler(
          servicer.FetchFindMissingSchemas,
          request_deserializer=hangar__service__pb2.FindMissingSchemasRequest.FromString,
          response_serializer=hangar__service__pb2.FindMissingSchemasReply.SerializeToString,
      ),
      'PushFindMissingCommits': grpc.unary_unary_rpc_method_handler(
          servicer.PushFindMissingCommits,
          request_deserializer=hangar__service__pb2.FindMissingCommitsRequest.FromString,
          response_serializer=hangar__service__pb2.FindMissingCommitsReply.SerializeToString,
      ),
      'PushFindMissingHashRecords': grpc.stream_stream_rpc_method_handler(
          servicer.PushFindMissingHashRecords,
          request_deserializer=hangar__service__pb2.FindMissingHashRecordsRequest.FromString,
          response_serializer=hangar__service__pb2.FindMissingHashRecordsReply.SerializeToString,
      ),
      'PushFindMissingLabels': grpc.stream_stream_rpc_method_handler(
          servicer.PushFindMissingLabels,
          request_deserializer=hangar__service__pb2.FindMissingLabelsRequest.FromString,
          response_serializer=hangar__service__pb2.FindMissingLabelsReply.SerializeToString,
      ),
      'PushFindMissingSchemas': grpc.unary_unary_rpc_method_handler(
          servicer.PushFindMissingSchemas,
          request_deserializer=hangar__service__pb2.FindMissingSchemasRequest.FromString,
          response_serializer=hangar__service__pb2.FindMissingSchemasReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'hangar.HangarService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
